import sys
import copy

def read_pla(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    header = []
    terms = []
    for line in lines:
        line = line.strip()
        if line.startswith('.i') or line.startswith('.o'):
            header.append(line)
        elif line != '' and not line.startswith('.e'):
            terms.append(line)
    return header, terms

def write_pla(filename, header, terms):
    with open(filename, 'w') as f:
        for line in header:
            f.write(f"{line}\n")
        for term in terms:
            f.write(f"{term}\n")
        f.write(".e\n")

def parse_terms(terms):
    parsed_terms = []
    for term in terms:
        if term.startswith('.'):
            continue
        parts = term.strip().split()
        if len(parts) == 2:
            input_term, output_term = parts
            parsed_terms.append((input_term, output_term))
        else:
            # Handle cases where output term is missing or malformed
            input_term = parts[0]
            output_term = ''
            parsed_terms.append((input_term, output_term))
    return parsed_terms

def combine_terms(term1, term2):
    combined = ''
    differences = 0
    for a, b in zip(term1, term2):
        if a == b:
            combined += a
        elif a != b and a != '-' and b != '-':
            combined += '-'
            differences += 1
        else:
            combined += '-'
            differences += 1
    if differences == 1:
        return combined
    else:
        return None

def remove_redundant_terms(terms):
    minimized_terms = []
    for term in terms:
        if term not in minimized_terms:
            minimized_terms.append(term)
    return minimized_terms

def minimize(parsed_terms):
    terms = [input_term for input_term, output_term in parsed_terms if output_term == '1']
    unchecked_terms = terms
    checked_terms = []
    while True:
        new_terms = []
        used_terms = set()
        for i in range(len(unchecked_terms)):
            for j in range(i + 1, len(unchecked_terms)):
                combined = combine_terms(unchecked_terms[i], unchecked_terms[j])
                if combined:
                    new_terms.append(combined)
                    used_terms.add(unchecked_terms[i])
                    used_terms.add(unchecked_terms[j])
        checked_terms.extend([term for term in unchecked_terms if term not in used_terms])
        if not new_terms:
            break
        unchecked_terms = list(set(new_terms))
    minimized_terms = remove_redundant_terms(checked_terms)
    return minimized_terms

def format_terms(minimized_terms, output_value):
    formatted_terms = []
    for term in minimized_terms:
        formatted_terms.append(f"{term} {output_value}")
    return formatted_terms

def update_header(header, num_terms):
    # Remove existing .p directive if present
    header = [line for line in header if not line.startswith('.p')]
    # Append updated .p directive with the number of product terms
    header.append(f".p {num_terms}")
    return header

def main():
    input_filename = 'input.pla'
    output_filename = 'output.pla'

    header, terms = read_pla(input_filename)
    parsed_terms = parse_terms(terms)
    minimized_terms = minimize(parsed_terms)
    formatted_terms = format_terms(minimized_terms, '1')

    # Update header with the number of product terms
    #header = update_header(header, len(formatted_terms))

    write_pla(output_filename, header, formatted_terms)
    print(f"Minimized PLA written to {output_filename}")

if __name__ == "__main__":
    main()
