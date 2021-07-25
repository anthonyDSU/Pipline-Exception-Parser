import hcl
import json

def open_parse_exep():
    with open('exceptions.json', 'r') as exceptions_file:
        exceptions = json.load(exceptions_file)
        #exceptions = json.load(type)
    for exception in exceptions:
        #exception_details = exception['exception_details']
        exception_details = exception['exception_details'][0]
    return exception_details

def policy_matching(policy_name):
    exp_details = open_parse_exep()
    matched_policies = []
    for exception in exp_details.keys():
        #for exception in exp_details.keys():
        for policies in policy_name.keys():
            if exception in policies:
                matched_policies.append(policies)
    return matched_policies

####################################
############### MAIN ###############
####################################

policy = 'sentinel.hcl'

with open(policy, 'r+') as sentinelhcl_file:
    exceptions = open_parse_exep()
    sentinelhcl = hcl.load(sentinelhcl_file)
    hcl_policies = sentinelhcl['policy']
    matched_policies = policy_matching(hcl_policies)
    
#exceptions = open_parse_exep()
#sentinelhcl = hcl.load(sentinelhcl_file)
#hcl_policies = sentinelhcl['policy']
#matched_policies = policy_matching(hcl_policies)
#for i in hcl_policies:
   #print(i)
	#if i in matched_policies:
	#    print(exceptions)
	#    enforcement_level = "Hi" #exceptions[i]
	#    hcl_policies[i]['enforcement_level'] = enforcement_level
	#hcl_parsed = hcl.dumps(hcl_policies)
	#sentinelhcl_file.write(hcl_parsed)

    for i in hcl_policies:
        #print(i)
        if i in matched_policies:
            print(exceptions)
            enforcement_level = "Hi" #exceptions[i]
            hcl_policies[i]['enforcement_level'] = enforcement_level
    hcl_parsed = hcl.dumps(hcl_policies)
    sentinelhcl_file.write(hcl_parsed)
