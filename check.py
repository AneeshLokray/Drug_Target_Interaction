# import pickle
# import networkx as nx
# from rdkit.Chem.rdmolfiles import MolFromSmiles, MolToSmiles
# import numpy as np

# # Open the pickle file for reading
# with open('data/kiba/Y', 'rb') as file:
#     loaded_data = pickle.load(file, encoding='latin1')


# print(loaded_data.shape)


# num_smiles = len({"11314340": "CC1=C2C=C(C=CC2=NN1)C3=CC(=CN=C3)OCC(CC4=CC=CC=C4)N", "24889392": "CC(C)(C)C1=CC(=NO1)NC(=O)NC2=CC=C(C=C2)C3=CN4C5=C(C=C(C=C5)OCCN6CCOCC6)SC4=N3", "11409972": "CCN1CCN(CC1)CC2=C(C=C(C=C2)NC(=O)NC3=CC=C(C=C3)OC4=NC=NC(=C4)NC)C(F)(F)F", "11338033": "C1CNCCC1NC(=O)C2=C(C=NN2)NC(=O)C3=C(C=CC=C3Cl)Cl", "10184653": "CN(C)CC=CC(=O)NC1=C(C=C2C(=C1)C(=NC=N2)NC3=CC(=C(C=C3)F)Cl)OC4CCOC4", "5287969": "CN1CCC(C(C1)O)C2=C(C=C(C3=C2OC(=CC3=O)C4=CC=CC=C4Cl)O)O", "6450551": "CNC(=O)C1=CC=CC=C1SC2=CC3=C(C=C2)C(=NN3)C=CC4=CC=CC=N4", "11364421": "CCC1C(=O)N(C2=CN=C(N=C2N1C3CCCC3)NC4=C(C=C(C=C4)C(=O)NC5CCN(CC5)C)OC)C", "9926054": "CC1=CC2=C(C=C1)N=C(C3=NC=C(N23)C)NCCN.Cl", "16007391": "CCN(CCCOC1=CC2=C(C=C1)C(=NC=N2)NC3=NNC(=C3)CC(=O)NC4=CC(=CC=C4)F)CCO", "5328940": "CN1CCN(CC1)CCCOC2=C(C=C3C(=C2)N=CC(=C3NC4=CC(=C(C=C4Cl)Cl)OC)C#N)OC", "11234052": "CC1=CC2=C(N1)C=CC(=C2F)OC3=NC=NN4C3=C(C(=C4)OCC(C)O)C", "11656518": "CN1C2=C(C=C(C=C2)OC3=CC(=NC=C3)C4=NC=C(N4)C(F)(F)F)N=C1NC5=CC=C(C=C5)C(F)(F)F", "6918454": "C1CC1CONC(=O)C2=C(C(=C(C=C2)F)F)NC3=C(C=C(C=C3)I)Cl", "156414": "C=CC(=O)NC1=C(C=C2C(=C1)C(=NC=N2)NC3=CC(=C(C=C3)F)Cl)OCCCN4CCOCC4", "9933475": "CC1=CC2=C(N1)C=CC(=C2F)OC3=NC=NC4=CC(=C(C=C43)OC)OCCCN5CCCC5", "11626560": "CC(C1=C(C=CC(=C1Cl)F)Cl)OC2=C(N=CC(=C2)C3=CN(N=C3)C4CCNCC4)N", "3062316": "CC1=C(C(=CC=C1)Cl)NC(=O)C2=CN=C(S2)NC3=NC(=NC(=C3)N4CCN(CC4)CCO)C", "156422": "CC1=CC=C(C=C1)N2C(=CC(=N2)C(C)(C)C)NC(=O)NC3=CC=C(C4=CC=CC=C43)OCCN5CCOCC5", "44150621": "CC(C(=O)O)O.CN1CCN(CC1)C2=CC3=C(C=C2)NC(=C4C(=C5C(=NC4=O)C=CC=C5F)N)N3.O", "176167": "CN1C=C(C2=CC=CC=C21)C3=C(C(=O)NC3=O)C4=CN(C5=CC=CC=C54)C6CCN(CC6)CC7=CC=CC=N7", "176870": "COCCOC1=C(C=C2C(=C1)C(=NC=N2)NC3=CC=CC(=C3)C#C)OCCOC", "42642645": "COC1=CC2=C(C=CN=C2C=C1OCCCN3CCOCC3)OC4=C(C=C(C=C4)NC(=O)C5(CC5)C(=O)NC6=CC=C(C=C6)F)F", "11717001": "C1CC(=NO)C2=C1C=C(C=C2)C3=CN(N=C3C4=CC=NC=C4)CCO", "16725726": "CCN1C2=C(C(=NC=C2OCC3CCCNC3)C#CC(C)(C)O)N=C1C4=NON=C4N", "11617559": "COC1=CC=C(C=C1)COC2=C(C=C(C=C2)CC3=CN=C(N=C3N)N)OC", "123631": "COC1=C(C=C2C(=C1)N=CN=C2NC3=CC(=C(C=C3)F)Cl)OCCCN4CCOCC4", "5291": "CC1=C(C=C(C=C1)NC(=O)C2=CC=C(C=C2)CN3CCN(CC3)C)NC4=NC=CC(=N4)C5=CN=CC=C5", "4908365": "CN1CCN(CC1)C(=O)C2=CC3=C(N2)C=CC(=C3)Cl", "11427553": "C1CN(CCN1)C(=O)C2=CC=C(C=C2)C=CC3=NNC4=CC=CC=C43", "208908": "CS(=O)(=O)CCNCC1=CC=C(O1)C2=CC3=C(C=C2)N=CN=C3NC4=CC(=C(C=C4)OCC5=CC(=CC=C5)F)Cl", "126565": "CC12C(CC(O1)N3C4=CC=CC=C4C5=C6C(=C7C8=CC=CC=C8N2C7=C53)CNC6=O)(CO)O", "11485656": "CC1=CC(=C(C=C1)F)NC(=O)NC2=CC=C(C=C2)C3=C4C(=CC=C3)NN=C4N", "9929127": "CC1=C(C=CC=N1)C(=O)NC2=C3C(=CC(=C2OC)Cl)C4=C(N3)C=NC=C4", "11712649": "C1C2=CN=C(N=C2C3=C(C=C(C=C3)Cl)C(=N1)C4=C(C=CC=C4F)F)NC5=CC=C(C=C5)C(=O)O", "10074640": "CC1=C(C=C(C=C1)NC(=O)C2=CC=C(C=C2)CN3CCN(CC3)C)NC4=NC(=CS4)C5=CN=CC=C5", "51004351": "CC12C(C(CC(O1)N3C4=CC=CC=C4C5=C6C(=C7C8=CC=CC=C8N2C7=C53)CNC6=O)N(C)C(=O)C9=CC=CC=C9)OC", "11667893": "CC1(CNC2=C1C=CC(=C2)NC(=O)C3=C(N=CC=C3)NCC4=CC=NC=C4)C", "9915743": "CCOC1=C(C=C2C(=C1)N=CC(=C2NC3=CC(=C(C=C3)OCC4=CC=CC=N4)Cl)C#N)NC(=O)C=CCN(C)C", "644241": "CC1=C(C=C(C=C1)C(=O)NC2=CC(=CC(=C2)N3C=C(N=C3)C)C(F)(F)F)NC4=NC=CC(=N4)C5=CN=CC=C5", "447077": "CN1C2=NC(=NC=C2C=C(C1=O)C3=C(C=CC=C3Cl)Cl)NC4=CC(=CC=C4)SC", "10461815": "CC1=C(NC(=C1C(=O)N2CCCC2CN3CCCC3)C)C=C4C5=C(C=CC(=C5)S(=O)(=O)CC6=C(C=CC=C6Cl)Cl)NC4=O", "9884685": "C1COCCN1C2=NC(=NC3=C2OC4=C3C=CC=N4)C5=CC(=CC=C5)O", "24180719": "CCCS(=O)(=O)NC1=C(C(=C(C=C1)F)C(=O)C2=CNC3=NC=C(C=C23)Cl)F", "25243800": "CC(C)N1C2=C(C(=C3C=C4C=C(C=CC4=N3)O)N1)C(=NC=N2)N", "10113978": "CC1=C(C=C(C=C1)NC2=NC=CC(=N2)N(C)C3=CC4=NN(C(=C4C=C3)C)C)S(=O)(=O)N", "17755052": "CS(=O)(=O)N1CCN(CC1)CC2=CC3=C(S2)C(=NC(=N3)C4=C5C=NNC5=CC=C4)N6CCOCC6", "11984591": "CC1(C(=O)NC2=C(O1)C=CC(=N2)NC3=NC(=NC=C3F)NC4=CC(=C(C(=C4)OC)OC)OC)C.C1=CC=C(C=C1)S(=O)(=O)O", "153999": "CN(C)CC1CCN2C=C(C3=CC=CC=C32)C4=C(C5=CN(CCO1)C6=CC=CC=C65)C(=O)NC4=O", "25127112": "C1CCC(C1)C(CC#N)N2C=C(C=N2)C3=C4C=CNC4=NC=N3.OP(=O)(O)O", "176155": "CS(=O)C1=CC=C(C=C1)C2=NC(=C(N2)C3=CC=NC=C3)C4=CC=C(C=C4)F", "24779724": "CN1C=C(C=N1)C2=NN3C(=NN=C3SC4=CC5=C(C=C4)N=CC=C5)C=C2", "3025986": "CC(C)(C)C1=CN=C(O1)CSC2=CN=C(S2)NC(=O)C3CCNCC3", "10138260": "CC1=C(NC(=C1C(=O)NCC(CN2CCOCC2)O)C)C=C3C4=C(C=CC(=C4)F)NC3=O", "10127622": "CN1C=NC2=C1C=C(C(=C2F)NC3=C(C=C(C=C3)Br)Cl)C(=O)NOCCO", "216239": "CNC(=O)C1=NC=CC(=C1)OC2=CC=C(C=C2)NC(=O)NC3=CC(=C(C=C3)Cl)C(F)(F)F", "44259": "CC12C(C(CC(O1)N3C4=CC=CC=C4C5=C6C(=C7C8=CC=CC=C8N2C7=C53)CNC6=O)NC)OC", "5329102": "CCN(CC)CCNC(=O)C1=C(NC(=C1C)C=C2C3=C(C=CC(=C3)F)NC2=O)C", "16038120": "CC(C)S(=O)(=O)C1=CC=CC=C1NC2=NC(=NC=C2Cl)NC3=C(C=C(C=C3)N4CCC(CC4)N5CCN(CC5)C)OC", "10427712": "C1=CC(=CC(=C1)O)C2=NC3=C(N=C2C4=CC(=CC=C4)O)N=C(N=C3N)N", "16722836": "CC1=CN=C(N=C1NC2=CC(=CC=C2)S(=O)(=O)NC(C)(C)C)NC3=CC=C(C=C3)OCCN4CCCC4", "3038522": "CC(C)OC1=CC=C(C=C1)NC(=O)N2CCN(CC2)C3=NC=NC4=CC(=C(C=C43)OC)OCCCN5CCCCC5", "9926791": "CC1CCN(CC1N(C)C2=NC=NC3=C2C=CN3)C(=O)CC#N", "5494449": "CC1=CC(=NN1)NC2=NC(=NC(=C2)N3CCN(CC3)C)SC4=CC=C(C=C4)NC(=O)C5CC5", "3038525": "C1=CC(=C(C(=C1)Cl)C2=C3C=CC(=NN3C=NC2=O)SC4=C(C=C(C=C4)F)F)Cl", "3081361": "CN1CCC(CC1)COC2=C(C=C3C(=C2)N=CN=C3NC4=C(C=C(C=C4)Br)F)OC", "9809715": "CN1CCN(CC1)CC(=O)N(C)C2=CC=C(C=C2)NC(=C3C4=C(C=C(C=C4)C(=O)OC)NC3=O)C5=CC=CC=C5", "151194": "C1=CC=C2C(=C1)C(=NN=C2NC3=CC=C(C=C3)Cl)CC4=CC=NC=C4"}
# )
# print(num_smiles)

# print(len(['C', 'N', 'O', 'S', 'F', 'Si', 'P', 'Cl', 'Br', 'Mg', 'Na','Ca', 'Fe', 'As', 'Al', 'I', 'B', 'V', 'K', 'Tl', 'Yb','Sb', 'Sn', 'Ag', 'Pd', 'Co', 'Se', 'Ti', 'Zn', 'H','Li', 'Ge', 'Cu', 'Au', 'Ni', 'Cd', 'In', 'Mn', 'Zr','Cr', 'Pt', 'Hg', 'Pb', 'Unknown']))

# a = [0,0,1,0,1,1,0,1]
# # b = []
# # b.append(a/sum(a))
# # print(b)
# print(sum(a))

# def atom_features(atom):
#     return np.array(one_of_k_encoding_unk(atom.GetSymbol(), ['C', 'N', 'O', 'S', 'F', 'Si', 'P', 'Cl', 'Br', 'Mg', 'Na','Ca', 'Fe', 'As', 'Al', 'I', 'B', 'V', 'K', 'Tl', 'Yb','Sb', 'Sn', 'Ag', 'Pd', 'Co', 'Se', 'Ti', 'Zn', 'H','Li', 'Ge', 'Cu', 'Au', 'Ni', 'Cd', 'In', 'Mn', 'Zr','Cr', 'Pt', 'Hg', 'Pb', 'Unknown']) +
#                     one_of_k_encoding(atom.GetDegree(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) +
#                     one_of_k_encoding_unk(atom.GetTotalNumHs(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) +
#                     one_of_k_encoding_unk(atom.GetImplicitValence(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) +
#                     [atom.GetIsAromatic()])

# def one_of_k_encoding(x, allowable_set):
#     if x not in allowable_set:
#         raise Exception("input {0} not in allowable set{1}:".format(x, allowable_set))
#     return list(map(lambda s: x == s, allowable_set))

# def one_of_k_encoding_unk(x, allowable_set):
#     """Maps inputs not in the allowable set to the last element."""
#     if x not in allowable_set:
#         x = allowable_set[-1]
#     return list(map(lambda s: x == s, allowable_set))
# def smile_to_graph(smile):
#     mol = MolFromSmiles(smile)
#     c_size = mol.GetNumAtoms()
    
#     features = []
#     for atom in mol.GetAtoms():
#         feature = atom_features(atom)
#         features.append( feature / sum(feature) )

#     edges = []
#     for bond in mol.GetBonds():
#         edges.append([bond.GetBeginAtomIdx(), bond.GetEndAtomIdx()])
#     g = nx.Graph(edges).to_directed()
    
#     edge_index = []
#     for e1, e2 in g.edges:
#         edge_index.append([e1, e2])
        
#     return c_size, features, edge_index
# g = smile_to_graph('CC1=C2C=C(C=CC2=NN1)C3=CC(=CN=C3)OCC(CC4=CC=CC=C4)N')
# print(len(g[1]))

import torch
import torch.nn as nn
import wandb
import random

# Define your model
class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.fc = nn.Linear(10, 1)  # Example linear layer

    def forward(self, x):
        x = self.fc(x)
        return x

# Initialize WandB run
wandb.init(
    project="my-awesome-project",
    config={
        "learning_rate": 0.02,
        "architecture": "CNN",
        "dataset": "CIFAR-100",
        "epochs": 10,
    }
)

# Create an instance of your model
model = MyModel()

# Define an optimizer and loss function (example)
optimizer = torch.optim.SGD(model.parameters(), lr=wandb.config.learning_rate)
criterion = nn.MSELoss()

# Simulate training
epochs = wandb.config.epochs
offset = random.random() / 5
for epoch in range(1, epochs + 1):
    # Generate random input data and target
    input_data = torch.randn(1, 10)
    target = torch.randn(1, 1)

    # Forward pass
    output = model(input_data)
    loss = criterion(output, target)

    # Backward pass and update weights
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # Log metrics and model weights to WandB
    wandb.log({"acc": 1 - loss.item(), "loss": loss.item()})
    wandb.watch(model)  # This line ensures that the model's gradients and weights are logged

wandb.finish()  # Finish the WandB run
