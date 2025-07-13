import os
import vertexai
from dotenv import load_dotenv
from vertexai import agent_engines

#relative imports
from multi_tool_agent.agent import root_agent

load_dotenv() 

#declaring environment variables that are to be initialized in cloud.
env_vars = {
    "MY_PROJECT_ID": os.getenv("MY_PROJECT_ID"),
    "MY_STAGING_BUCKET": os.getenv("MY_STAGING_BUCKET"),
    "MY_LOCATION": os.getenv("MY_LOCATION")
}

PROJECT_ID = os.getenv("MY_PROJECT_ID")
LOCATION = os.getenv("MY_LOCATION")
STAGING_BUCKET = os.getenv("MY_STAGING_BUCKET")

# Init Vertex AI
vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=STAGING_BUCKET,
)

extra_packages = ["multi_tool_agent"]
requirements = [
    "google-cloud-aiplatform[agent_engines,adk]",
    "cloudpickle==3.1.1",
    "pandas==2.3.1",
    "setuptools==78.1.1",
]

gcs_dir_name = "linkedIn-ghostwriter-agent" 
remote_app = agent_engines.create(
    agent_engine=root_agent,
    display_name="linkedIn-ghostwriter-agent",
    requirements=requirements,
    extra_packages=extra_packages,
    gcs_dir_name=gcs_dir_name,
    env_vars=env_vars,
)

print("Agent deployment complete, Agent is deployed at:", remote_app.resource_name)


