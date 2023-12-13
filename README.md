install node >= 16 
https://nodejs.org/en/download


cd frontend


npm i


On Unix-like (Linux, macOS, Git bash, etc.):

export NODE_OPTIONS=--openssl-legacy-provider
On Windows command prompt:

set NODE_OPTIONS=--openssl-legacy-provider
On PowerShell:

$env:NODE_OPTIONS = "--openssl-legacy-provider"


npm run build

L
rm -rf node_modules

W
npm i -g rm
rm -rf node_modules