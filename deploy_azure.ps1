# Azure Deployment Steps
$resourceGroup = "CamFiestaGroup"
$location = "eastus"
$appName = "camfiesta"
$storageName = "camfiestastore"

# Login to Azure (uncomment when ready)
# az login

# Create Resource Group
az group create --name $resourceGroup --location $location

# Create Storage Account
az storage account create `
    --name $storageName `
    --resource-group $resourceGroup `
    --location $location `
    --sku Standard_LRS

# Get Storage Key
$storageKey = $(az storage account keys list --resource-group $resourceGroup --account-name $storageName --query "[0].value" -o tsv)

# Create Container
az storage container create `
    --name media `
    --account-name $storageName `
    --account-key $storageKey `
    --public-access blob

# Create App Service Plan
az appservice plan create `
    --name ${appName}-plan `
    --resource-group $resourceGroup `
    --sku B1 `
    --is-linux

# Create Web App
az webapp create `
    --resource-group $resourceGroup `
    --plan ${appName}-plan `
    --name $appName `
    --runtime "PYTHON|3.10" `
    --deployment-local-git

# Configure App Settings
az webapp config appsettings set `
    --resource-group $resourceGroup `
    --name $appName `
    --settings `
    AZURE_ACCOUNT_NAME=$storageName `
    AZURE_ACCOUNT_KEY=$storageKey `
    AZURE_CONTAINER=media `
    DJANGO_SETTINGS_MODULE=camfiesta.production `
    GEMINI_API_KEY=$env:GEMINI_API_KEY `
    WEBSITES_PORT=8000

# Enable logging
az webapp log config `
    --resource-group $resourceGroup `
    --name $appName `
    --web-server-logging filesystem

# Deploy the code
git init
git add .
git commit -m "Initial commit for Azure deployment"
az webapp up --name $appName --resource-group $resourceGroup --runtime "PYTHON|3.10"

# Note: After deployment, run migrations
# az webapp ssh --name $appName --resource-group $resourceGroup
# python manage.py migrate
# python manage.py collectstatic --noinput
