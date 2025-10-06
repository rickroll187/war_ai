// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;
contract CTISharing {
    address public owner;
    mapping(address => bool) public approved;
    event Shared(address indexed who, string ipfs_cid);

    constructor(){ owner = msg.sender; }

    function setApproved(address who, bool val) external {
        require(msg.sender == owner, "only owner");
        approved[who]=val;
    }

    function shareCTI(string calldata ipfs_cid) external {
        require(approved[msg.sender],"not approved");
        emit Shared(msg.sender, ipfs_cid);
    }
}
