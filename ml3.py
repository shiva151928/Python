# Training data
concepts = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change']
]

target = ['Yes', 'Yes', 'No', 'Yes']

def candidate_elimination(concepts, target):
    specific_h = concepts[0].copy()
    general_h = [['?' for _ in range(len(specific_h))]
                 for _ in range(len(specific_h))]

    for i, h in enumerate(concepts):
        if target[i] == 'Yes':
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
        else:
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'

    final_g = [g for g in general_h if g != ['?'] * len(specific_h)]
    return specific_h, final_g

S, G = candidate_elimination(concepts, target)

print("Final Specific Hypothesis:")
print(S)

print("\nFinal General Hypothesis:")
for g in G:
    print(g)
