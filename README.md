# Pipline-Exception-Parser

Tool Objective: Sentinel Exceptions Parser Script

> python3 pipline_exceptions_parser.py

Sentinel is an embedded policy-as-code framework integrated with the HashiCorp Enterprise products. It enables fine-grained, logic-based policy decisions, and can be extended to use information from external sources. It basically has an open policy framework, OPA (openpolicyagent), the Sentinel language uses OPA and golang. Sentinel policy looks like the following:

https://github.com/hashicorp/terraform-guides/blob/master/governance/third-generation/aws/restrict-ec2-instance-type.sentinel
- restrict-ec2-instance-type.sentinel Policy Example
- It looks at your terrafrom plan, and checks to see if your instance type matches line 10. (allowed_types = ["t2.small", "t2.medium", "t2.large"])
- If the instance is not part of the list, it fails the IAC deployment.
- Line 17 does the evaluation.

https://github.com/hashicorp/terraform-guides/blob/master/governance/third-generation/aws/sentinel.hcl
- Policy enforcement is done through sentinel.hcl file which is present in the root of all sentinel policy dir.
- Policy Example
policy "protect-against-rds-instance-deletion" { # Defines Policy Name
source = "./protect-against-rds-instance-deletion.sentinel" # Defines Policy Location
enforcement_level = "advisory" #Defines Policy Enforcement Level (3 Enforcement Levels: Advisory, soft-mandatory, hard-mandatory)

pipline_exceptions_parser.py
- Exceptions Parser Script
- This Takes in exceptions.json, parses it for enforcement_level and policy name, then rewrites the sentinel.hcl file.
- In order to enforce the policy, terraform looks for sential.hcl
- python3 pipeline_exceptions_parser.py
- Modify policy enforcement_level based on what you set in the JSON file.

Usefulness:
You have multiple exceptions in part of a JSON object, when you have multiple policies and exceptions (can be hundreds), this script basically handles all of this for you. The script is checking if the enforcement_level in the sentinel HCL matches up to what is within the exceptions.json.

Direction and Future Direction: Need to load it into golang so it writes out proper output in hcl form. Overall, I'd suggest starting with OPA rather than Sentinel because it's useful in more contexts and is easier to get started because of the availability of documentation, size of the community, and open-source model. The time you spend mastering OPA will not be lost even if you end up just using Sentinel for now.
