// Simple cache for units per type
const unitsCache = {};

const tabs = document.querySelectorAll(".tab");
const typeInput = document.getElementById("type");
const fromSelect = document.getElementById("from-unit");
// API base URL helper
const API_BASE = "http://localhost:5000";
function apiFetch(path, options) {
    return fetch(API_BASE + path, options);
}

const toSelect = document.getElementById("to-unit");
const valueInput = document.getElementById("value");
const convertBtn = document.getElementById("convert-btn");
const statusSpan = document.getElementById("status");
const modal = document.getElementById("result-modal");
const resultText = document.getElementById("result-text");
const closeModal = document.getElementById("close-modal");
const form = document.getElementById("convert-form");

let activeType = "height";

function setLoading(isLoading) {
    if (isLoading) {
        convertBtn.disabled = true;
        statusSpan.innerHTML = '<span class="spinner"></span> Loading…';
        form.classList.add("loading");
    } else {
        convertBtn.disabled = false;
        statusSpan.textContent = "";
        form.classList.remove("loading");
    }
}

// Add spinner CSS
if (!document.getElementById('spinner-style')) {
    const style = document.createElement('style');
    style.id = 'spinner-style';
    style.textContent = `.spinner { display: inline-block; width: 16px; height: 16px; border: 2px solid #2563eb; border-top: 2px solid #fff; border-radius: 50%; animation: spin 0.7s linear infinite; vertical-align: middle; margin-right: 6px; } @keyframes spin { 100% { transform: rotate(360deg); } }`;
    document.head.appendChild(style);
}

// populate select options
function populateUnits(type, units) {
    const buildOptions = (select) => {
        select.innerHTML = "";
        units.forEach((u) => {
            const opt = document.createElement("option");
            opt.value = u.id;
            opt.textContent = u.label;
            select.appendChild(opt);
        });
    };
    buildOptions(fromSelect);
    buildOptions(toSelect);
}

// fetch units from API (with caching)
async function loadUnits(type) {
    if (unitsCache[type]) {
        populateUnits(type, unitsCache[type]);
        return unitsCache[type];
    }
    setLoading(true);
    try {
        const res = await apiFetch(`/api/units?type=${encodeURIComponent(type)}`);
        if (!res.ok) throw new Error("Failed to load units");
        const data = await res.json();
        unitsCache[type] = data;
        populateUnits(type, data);
        return data;
    } catch (err) {
        console.error(err);
        statusSpan.textContent = "Failed to load units";
        populateUnits(type, [{ id: "", label: "— no units —" }]);
    } finally {
        setLoading(false);
    }
}

// Input validation
function validateForm() {
    let valid = true;
    let msg = "";
    if (!fromSelect.value) {
        valid = false;
        msg = "Select a 'From' unit.";
    } else if (!toSelect.value) {
        valid = false;
        msg = "Select a 'To' unit.";
    } else if (!valueInput.value || isNaN(valueInput.value)) {
        valid = false;
        msg = "Enter a valid value.";
    }
    if (!valid) {
        statusSpan.textContent = msg;
    }
    return valid;
}

// perform conversion via API
async function convert() {
    if (!validateForm()) return;
    const type = activeType;
    const from_unit = fromSelect.value;
    const to_unit = toSelect.value;
    const value = Number(valueInput.value);

    setLoading(true);
    try {
        const res = await apiFetch("/api/convert", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                type,
                from_unit,
                to_unit,
                value,
            }),
        });
        if (!res.ok) {
            const err = await res.json();
            throw new Error(err.detail || "Conversion failed");
        }
        const json = await res.json();
        resultText.textContent = json.formatted ?? `${json.result}`;
        modal.style.display = "flex";
    } catch (err) {
        console.error(err);
        statusSpan.textContent = err.message || "Conversion error";
    } finally {
        setLoading(false);
    }
}

// Accessibility: keyboard navigation for tabs
tabs.forEach((tab, idx) => {
    tab.addEventListener("click", async () => {
        tabs.forEach((t) => {
            t.classList.remove("active");
            t.setAttribute("aria-selected", "false");
        });
        tab.classList.add("active");
        tab.setAttribute("aria-selected", "true");
        activeType = tab.dataset.type;
        typeInput.value = activeType;
        statusSpan.textContent = "";
        await loadUnits(activeType);
    });
    tab.addEventListener("keydown", (e) => {
        if (e.key === "ArrowRight") {
            tabs[(idx + 1) % tabs.length].focus();
        } else if (e.key === "ArrowLeft") {
            tabs[(idx - 1 + tabs.length) % tabs.length].focus();
        }
    });
    tab.setAttribute("tabindex", "0");
});

convertBtn.addEventListener("click", convert);
closeModal.addEventListener("click", () => {
    modal.style.display = "none";
    resultText.textContent = "";
});

// Responsive: adjust modal for mobile
window.addEventListener("resize", () => {
    if (window.innerWidth < 600) {
        modal.querySelector(".card").style.minWidth = "180px";
    } else {
        modal.querySelector(".card").style.minWidth = "260px";
    }
});

// initial load
loadUnits(activeType);
