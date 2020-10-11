# Prerequisite:
# we need to install env-cmd package as globale first: `npm install -g env-cmd`

# start app2 service without recreate or start deps
env-cmd -f ./local-dev.env docker-compose up --no-deps  app2