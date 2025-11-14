import { githubApi } from "./api";

(async () => {
    const username = String(process.argv[2]);
    if (!username) {
        console.log("Usage: npm start <username>");
        process.exit(1);
    }
    const response = await githubApi(username);
    response.map((res) => console.log(res));
})();
