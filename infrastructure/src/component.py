from BBC.AWS.CloudFormation.Common.Component import Component

component = Component("sarafs02-cosmos-train")
component.set_health_check_url("/status")
component.render()