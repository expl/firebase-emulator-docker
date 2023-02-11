# Firebase-emulator-docker
Multi-platform and simple to use Firebase emulator Docker container

# Environment configuration attributes
* `PROJECT_ID`: ID of Firebase project, prefix with `demo-` to [make sure no live resources are being used](https://firebase.google.com/docs/emulator-suite/connect_auth#choose_a_firebase_project).
* `EMULATORS`: Space separated list of services to emulate/enable. Possible entries are: `auth`, `firestore`, `pubsub`, `storage`, `database` and `functions`. Emulator UI is always enabled.

# Ports to expose for each service emulated
|Service  |Port    |
|---------|--------|
|auth     | 9099   |
|firestore| 8080   |
|pubub    | 8085   |
|storage  | 9199   |
|database | 9000   |
|functions| 5001   |
|UI       | 4000   |

# Example compose file
```yaml
name: firebase-emulator-workspace
services:
  firebase-emulator:
    container_name: emulator
    image: kpetrikas/firebase-emulator:latest
    ports:
      # Emulator UI
      - "4000:4000"
      # Auth
      - "9099:9099"
      # Firestore
      - "8080:8080"
    environment:
      PROJECT_ID: demo-firebase-project
      EMULATORS: auth firestore
```