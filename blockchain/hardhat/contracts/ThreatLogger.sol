// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract ThreatLogger {
    struct Entry { address reporter; uint256 ts; string ipfs_cid; string severity; string summary; }
    Entry[] public entries;
    event EntryLogged(uint256 indexed id, address reporter, string ipfs_cid, string severity);

    function logThreat(string calldata ipfs_cid, string calldata severity, string calldata summary) external returns (uint256) {
        entries.push(Entry(msg.sender, block.timestamp, ipfs_cid, severity, summary));
        uint256 id = entries.length - 1;
        emit EntryLogged(id, msg.sender, ipfs_cid, severity);
        return id;
    }
    function count() external view returns (uint256) { return entries.length; }
}
