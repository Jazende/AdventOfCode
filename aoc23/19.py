import re
import copy

with open('input_19.txt', 'r') as f:
    raw_inputs = f.read()

raw_inputs = '''px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}'''

########################## DAY 19 SETUP ########################### 

re_parts = re.compile('{x=(?P<x>\d+),m=(?P<m>\d+),a=(?P<a>\d+),s=(?P<s>\d+)}')
re_ruleset = re.compile('(?P<rule_name>[0-9a-z]+){(?P<rules>.+?)}')
re_rule = re.compile('(?P<category>[xmas])?(?P<operation>[><])?(?P<operand>(\d+))?\:?(?P<workflow>[a-zA-Z]+)')

raw_rules, raw_parts = raw_inputs.strip().split('\n\n')
raw_rules_list = raw_rules.split('\n')
parts = [re_parts.match(part).groupdict() for part in raw_parts.split('\n')]


rules = {}
for rule in raw_rules_list:
    rules_match = re_ruleset.match(rule).groupdict()
    rules[rules_match['rule_name']] = [
        re_rule.match(rule).groupdict() for rule in rules_match['rules'].split(',')[:-1]
    ]
    rules[rules_match['rule_name']].append(
        {'category': None, 'operation': None, 'operand': None, 'workflow': rules_match['rules'].split(',')[-1]}
    )

########################## DAY 19 PART 1 ########################## 

def check_operation(l_value, operantion, r_value):
    if operantion == '<':
        return int(l_value) < int(r_value)
    return int(l_value) > int(r_value)

for part in parts:
    workflow = 'in'

    while True:
        if workflow == 'R':
            part['result'] = 'R'
            break
        elif workflow == 'A':
            part['result'] = 'A'
            break

        rule_set = rules[workflow]

        for rule in rule_set:
            if rule['category'] is None:
                workflow = rule['workflow']
                break
            else:
                if check_operation(part[rule['category']], rule['operation'], rule['operand']):
                    workflow = rule['workflow']
                    break

print(sum(sum(int(value) for key, value in part.items() if not key == 'result') for part in parts if part['result'] == 'A'))

########################## DAY 19 PART 2 ########################## 

total_sum = 0

def recursive_rules(workflow, rule_index, parts, all_rules):
    global total_sum
    if workflow == 'A':
        str_parts = ""
        str_parts += f"{parts['x']['min']:>4} < x < {parts['x']['max']:>4} | {parts['x']['max'] - (parts['x']['min'] - 1):>4} | "
        str_parts += f"{parts['m']['min']:>4} < m < {parts['m']['max']:>4} | {parts['m']['max'] - (parts['m']['min'] - 1):>4} | "
        str_parts += f"{parts['a']['min']:>4} < a < {parts['a']['max']:>4} | {parts['a']['max'] - (parts['a']['min'] - 1):>4} | "
        str_parts += f"{parts['s']['min']:>4} < s < {parts['s']['max']:>4} | {parts['s']['max'] - (parts['s']['min'] - 1):>4}"
        total = 1
        total *= (parts['x']['max'] - (parts['x']['min'] - 1))
        total *= (parts['m']['max'] - (parts['m']['min'] - 1))
        total *= (parts['a']['max'] - (parts['a']['min'] - 1))
        total *= (parts['s']['max'] - (parts['s']['min'] - 1))
        # print('Accepted ', str_parts, "\t", str(total).rjust(15))
        total_sum += total
        return 
    elif workflow == 'R':
        # str_parts = ""
        # str_parts += f"{parts['x']['min']:>4} < x < {parts['x']['max']:>4} | {parts['x']['max'] - (parts['x']['min'] - 1):>4} | "
        # str_parts += f"{parts['m']['min']:>4} < m < {parts['m']['max']:>4} | {parts['m']['max'] - (parts['m']['min'] - 1):>4} | "
        # str_parts += f"{parts['a']['min']:>4} < a < {parts['a']['max']:>4} | {parts['a']['max'] - (parts['a']['min'] - 1):>4} | "
        # str_parts += f"{parts['s']['min']:>4} < s < {parts['s']['max']:>4} | {parts['s']['max'] - (parts['s']['min'] - 1):>4}"
        # total = 1
        # total *= (parts['x']['max'] - (parts['x']['min'] - 1))
        # total *= (parts['m']['max'] - (parts['m']['min'] - 1))
        # total *= (parts['a']['max'] - (parts['a']['min'] - 1))
        # total *= (parts['s']['max'] - (parts['s']['min'] - 1))
        # print('Rejected ', str_parts, "\t", str(total).rjust(15))
        return

    if all_rules[workflow][rule_index]['operation'] == '>':
        parts_if_match = copy.deepcopy(parts)
        parts_if_match[all_rules[workflow][rule_index]['category']]['min'] = max(
            int( all_rules[workflow][rule_index]['operand'] ) + 1,
            parts[all_rules[workflow][rule_index]['category']]['min']
        )
        recursive_rules(all_rules[workflow][rule_index]['workflow'], 0, parts_if_match, all_rules)

        parts_if_not_match = copy.deepcopy(parts)
        parts_if_not_match[all_rules[workflow][rule_index]['category']]['max'] = min(
            int( all_rules[workflow][rule_index]['operand'] ),
            parts[all_rules[workflow][rule_index]['category']]['max']
        )
        recursive_rules(workflow, rule_index+1, parts_if_not_match, all_rules)
    elif all_rules[workflow][rule_index]['operation'] == '<':
        parts_if_match = copy.deepcopy(parts)
        parts_if_match[all_rules[workflow][rule_index]['category']]['max'] = min(
            int( all_rules[workflow][rule_index]['operand'] ) - 1,
            parts[all_rules[workflow][rule_index]['category']]['max']
        )
        recursive_rules(all_rules[workflow][rule_index]['workflow'], 0, parts_if_match, all_rules)

        parts_if_not_match = copy.deepcopy(parts)
        parts_if_not_match[all_rules[workflow][rule_index]['category']]['min'] = max(
            int( all_rules[workflow][rule_index]['operand'] ),
            parts[all_rules[workflow][rule_index]['category']]['min']
        )
        recursive_rules(workflow, rule_index+1, parts_if_not_match, all_rules)
    elif all_rules[workflow][rule_index]['operation'] == None:
        recursive_rules(all_rules[workflow][rule_index]['workflow'], 0, parts, all_rules)

parts_requirements = {
    'x': {'min': 1, 'max': 4000},
    'm': {'min': 1, 'max': 4000},
    'a': {'min': 1, 'max': 4000},
    's': {'min': 1, 'max': 4000},
}

recursive_rules('in', 0, parts_requirements, rules)

print(total_sum)
