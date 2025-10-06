async function main() {
  const names = ["ThreatLogger","CTISharing","IncidentResponse"];
  for (const name of names) {
    const Factory = await ethers.getContractFactory(name);
    const contract = await Factory.deploy();
    await contract.deployed();
    console.log(`${name} deployed to ${contract.address}`);
  }
}

main().catch(err => { console.error(err); process.exit(1); });
