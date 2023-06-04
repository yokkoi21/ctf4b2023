const crypto = require('crypto');

function generateRandomString() {
    return crypto.randomBytes(16).toString("hex");
}

console.log(generateRandomString());
