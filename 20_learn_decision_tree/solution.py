from collections import Counter
import math


def entropy(examples, target_attribute):
    class_counts = Counter(example[target_attribute] for example in examples)
    total_examples = len(examples)
    entropy_value = 0.0

    for count in class_counts.values():
        probability = count / total_examples
        if probability > 0:
            entropy_value -= probability * math.log2(probability)
            # this comes from Shannon’s entropy formula, which measures uncertainty in a dataset.


    return entropy_value


def information_gain(examples, attribute, target_attribute):
    total_entropy = entropy(examples, target_attribute)
    total_examples = len(examples)
    weighted_entropy = 0.0

    value_groups = {}
    for example in examples:
        value = example[attribute]
        if value not in value_groups:
            value_groups[value] = []
        value_groups[value].append(example)

    # Calculate weighted entropy for each value group
    for group in value_groups.values():
        group_probability = len(group) / total_examples
        weighted_entropy += group_probability * entropy(group, target_attribute)

    return total_entropy - weighted_entropy


def plurality_value(examples, target_attribute):
    """
    Parameters:
        examples (list): List of examples.
        target_attribute (str): The name of the target attribute.

    Returns:
        str: The most common value of the target attribute.
    """
    class_counts = Counter(example[target_attribute] for example in examples)
    return class_counts.most_common(1)[0][0]


def decision_tree_learning(examples, attributes, target_attribute, parent_examples=None):
    """
    Parameters:
        examples (list): List of examples.
        attributes (list): List of attributes to consider for splitting.
        target_attribute (str): The name of the target attribute.
        parent_examples (list): Parent examples (used for handling empty subsets).

    Returns:
        dict: A nested dictionary representing the decision tree.
    """
    if not examples:
        return plurality_value(parent_examples, target_attribute)

    classifications = {example[target_attribute] for example in examples}
    if len(classifications) == 1:
        return classifications.pop()

    if not attributes:
        return plurality_value(examples, target_attribute)

    best_attribute = max(attributes, key=lambda attr: information_gain(examples, attr, target_attribute))

    tree = {best_attribute: {}}

    remaining_attributes = [attr for attr in attributes if attr != best_attribute]

    value_groups = {}
    for example in examples:
        value = example[best_attribute]
        if value not in value_groups:
            value_groups[value] = []
        value_groups[value].append(example)

    # Recursively build subtrees for each value of the best attribute
    for value, group in value_groups.items():
        subtree = decision_tree_learning(group, remaining_attributes, target_attribute, examples)
        tree[best_attribute][value] = subtree

    return tree


if __name__ == "__main__":
    examples = [
        {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'},
        {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'No'},
        {'Outlook': 'Overcast', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
        {'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
        {'Outlook': 'Rain', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
        {'Outlook': 'Rain', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'No'},
        {'Outlook': 'Overcast', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'Yes'},
        {'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'},
        {'Outlook': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
        {'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
        {'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'Yes'},
        {'Outlook': 'Overcast', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'Yes'},
        {'Outlook': 'Overcast', 'Temperature': 'Hot', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'}
    ]
    attributes = ['Outlook', 'Temperature', 'Humidity', 'Wind']
    target_attribute = 'PlayTennis'

    tree = decision_tree_learning(examples, attributes, target_attribute)
    print(tree)
