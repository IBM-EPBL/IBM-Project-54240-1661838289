
  window.watsonAssistantChatOptions = {
    integrationID: "40e2e583-2bd1-4c3d-8e13-73a5f2d2bf7c", // The ID of this integration.
    region: "au-syd", // The region your integration is hosted in.
    serviceInstanceID: "2fe20232-f2c4-482c-a137-66a6e34214ac", // The ID of your service instance.
    onLoad: function(instance) { instance.render(); }
  };
  setTimeout(function(){
    const t=document.createElement('script');
    t.src="https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + (window.watsonAssistantChatOptions.clientVersion || 'latest') + "/WatsonAssistantChatEntry.js";
    document.head.appendChild(t);
  });