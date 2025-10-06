// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;
contract IncidentResponse {
    struct Incident { string id; string ipfs; bool mitigated; uint256 ts; }
    Incident[] public incidents;
    event Recorded(string id, string ipfs);
    event Mitigated(string id);

    function record(string calldata id, string calldata ipfs) external {
        incidents.push(Incident(id, ipfs, false, block.timestamp));
        emit Recorded(id, ipfs);
    }
    function markMitigated(uint idx) external {
        incidents[idx].mitigated = true;
        emit Mitigated(incidents[idx].id);
    }
}
