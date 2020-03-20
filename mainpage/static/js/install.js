window.addEventListener('beforeinstallprompt', saveBeforeInstallPromptEvent);
deferredInstallPrompt = evt;
installButton.removeAttribute('hidden');
// CODELAB: Add code show install prompt & hide the install button.
deferredInstallPrompt.prompt();
// Hide the install button, it can't be called twice.
evt.srcElement.setAttribute('hidden', true);
// CODELAB: Add event listener for appinstalled event
window.addEventListener('appinstalled', logAppInstalled);
// CODELAB: Add code to log the event
console.log('Aplicación meteorológica fue instalada.', evt);