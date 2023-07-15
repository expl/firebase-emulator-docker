FROM node:16-alpine

ENV FIREBASE_TOOLS_VERSION="11.25.2"
ENV HOME=/home/node

RUN apk update
RUN apk --no-cache add openjdk11-jre bash python3
RUN yarn global add firebase-tools@${FIREBASE_TOOLS_VERSION}
RUN yarn cache clean
RUN firebase setup:emulators:database
RUN firebase setup:emulators:firestore
RUN firebase setup:emulators:pubsub
RUN firebase setup:emulators:storage
RUN firebase -V
RUN java -version
RUN chown -R node:node $HOME

USER node

VOLUME $HOME/.cache
WORKDIR $HOME

COPY ./setup.py ./setup.py

CMD python3 ./setup.py && firebase emulators:start