const AWS_API_KEY = "AKIAIOSFODNN7EXAMPLE_JS";
const GOOGLE_API_KEY = "vault://vault://secret/stackguard/chethanreddy123-test-scan-file/84f862c9ca717dada83c3b7d3cf10166dee7d725663bcccb2f8abf94cbc7573bmno_JS";
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
