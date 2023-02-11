import os
import json
from typing import Optional, List

HOST = "0.0.0.0"

# To add new emulated services simply add new entries here with their port numbers
EMULATOR_PORTS = {
    "auth": 9099,
    "firestore": 8080,
    "pubsub": 8085,
    "storage": 9199,
    "database": 9000,
    "functions": 5001
}

BASE_CONF = {
    "singleProjectMode": True,
    "emulators":{
        "ui": {
            "enabled": True,
            "host": "0.0.0.0",
            "port": 4000
        }
    }
}


def setup_firebaserc(project_id: str):
    """
    Create `.firebaserc` file with project ID set
    """
    json.dump(
        {
            "projects": {
                "default": project_id
            }
        },
        open(".firebaserc", "w")
    )


def setup_firebasejson(emulators: List[str]):
    """
    Create `firebase.json` configuration file based on emulator selection from environment
    """
    for emulator in emulators:
        port: Optional[int] = EMULATOR_PORTS.get(emulator, None)

        if port is None:
            raise ValueError(f"Emulator '{emulator}' is unknown")
        
        BASE_CONF["emulators"][emulator] = {
            "host": "0.0.0.0",
            "port": port
        }
    
    json.dump(BASE_CONF, open("firebase.json", "w"))


def setup():
    """
    Read environment configuration and output Firebase configuration files
    """
    project_id: Optional[str] = os.getenv("PROJECT_ID", None)

    if project_id is None:
        raise AttributeError("Environment variable 'PROJECT_ID' is not set")
    
    setup_firebaserc(project_id)

    emulators_str: Optional[str] = os.getenv("EMULATORS", None) 
    if emulators_str is None:
        raise AttributeError("Environment variable 'EMULATORS' is not set")
    
    emulators: List[str] = emulators_str.split()
    setup_firebasejson(emulators)


if __name__ == "__main__":
    setup()
