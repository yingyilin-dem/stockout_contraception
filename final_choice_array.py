# Step 1: Original choices (intended method before stockout)
choice_array[switch_iinds] = np.array(list(mcp.method_idx))[these_choices]  # Keep this line

# Step 2: Apply stockout to determine actual method received
final_choice_array = np.copy(choice_array)  # Start with intended choices

stockout_probs = ppl.pars.get('stockout_probs', {})

for j, person_idx in enumerate(switch_iinds):
    method_idx = choice_array[person_idx]
    method_obj = next((v for v in self.methods.values() if v.idx == method_idx), None)
    method_name = method_obj.name if method_obj is not None else 'none'
    prob = stockout_probs.get(method_name, 0.0)

    if np.random.random() <= prob:  # Stocked out
        final_choice_array[person_idx] = 0  # Assign 'none'
