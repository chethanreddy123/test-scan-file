const vault = require('node-vault')({
    endpoint: process.env.VAULT_ADDR,
    token: process.env.VAULT_TOKEN
});

const AWS_API_KEY = "AKIAIOSFODNN7EXAMPLE_JS";
const GOOGLE_API_KEY = await (async () => {
    try {
        const result = await vault.read('secret/chethanreddy123/test-scan-file/main.js');
        return result.data.data.secret;
    } catch (error) {
        console.error("Error fetching GOOGLE_API_KEY from Vault:", error);
        throw error; // Terminate script if a critical secret cannot be fetched
    }
})();
const GITHUB_TOKEN = "ghp_DummyToken1234567890AbCdEfGhIjKlMnOpQrStUv_JS";

function fetchAwsData() {
    console.log("Fetching AWS data in JS with key:", AWS_API_KEY);
}

function fetchGoogleData() {
    console.log("Fetching Google data in JS with key:", GOOGLE_API_KEY);
}

function fetchGithubData() {
    console.log("Fetching GitHub data in JS with key:", GITHUB_TOKEN);
}

fetchAwsData();
fetchGoogleData();
fetchGithubData();