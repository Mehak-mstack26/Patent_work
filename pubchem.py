import requests

pugrest_prolog = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
pugrest_input = "compound/name/Trifloxystrobin"

pugrest_operation = "property/MolecularFormula"
pugrest_output = "txt"

pugrest_url = "/".join((pugrest_prolog, pugrest_input, pugrest_operation, pugrest_output))
print("REQUEST URL:", pugrest_url)

res = requests.get(pugrest_url)

if res.status_code == 200:
    print("OUTPUT    :", res.text.strip())
else:
    print(f"Error: Request failed with status code {res.status_code}")
    print(res.text)

pugrest_operation = "property/MolecularWeight,CanonicalSMILES,InChIKey"
pugrest_output = "JSON"

pugrest_url = "/".join((pugrest_prolog, pugrest_input, pugrest_operation, pugrest_output))
print("REQUEST URL:", pugrest_url)

res = requests.get(pugrest_url)

if res.status_code == 200:
    data = res.json()
    properties = data["PropertyTable"]["Properties"][0]
    print("OUTPUT:")
    print(f"  Molecular Weight: {properties['MolecularWeight']}")
    print(f"  Canonical SMILES: {properties['CanonicalSMILES']}")
    print(f"  InChIKey: {properties['InChIKey']}")

else:
    print(f"Error: Request failed with status code {res.status_code}")
    print(res.text)