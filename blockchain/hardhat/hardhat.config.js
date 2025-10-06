require("@nomicfoundation/hardhat-toolbox");
require("dotenv").config();
module.exports = {
  solidity: "0.8.17",
  networks: {
    local: { url: "http://127.0.0.1:8545", chainId: 1337 },
    sepolia: { url: process.env.SEPOLIA_URL || "", accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [] }
  }
};
