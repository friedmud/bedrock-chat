import { BedrockChatParametersInput } from "./lib/utils/parameter-models";

export const bedrockChatParams = new Map<string, BedrockChatParametersInput>();
// You can define multiple environments and their parameters here
// bedrockChatParams.set("dev", {});

// If you define "default" environment here, parameters in cdk.json are ignored
// bedrockChatParams.set("default", {});

// Define parameters for the default environment
bedrockChatParams.set("default", {
    bedrockRegion: "us-east-1",
    selfSignUpEnabled: false,
    enableBotStore: false,
    autoJoinUserGroups: [],
    tokenValidMinutes: 120,
  });
  
  // Define parameters for additional environments
  bedrockChatParams.set("dev", {
    bedrockRegion: "us-east-1",
    selfSignUpEnabled: false,
    enableBotStore: true,
    autoJoinUserGroups: [],
    tokenValidMinutes: 120,
  });
  
  bedrockChatParams.set("prod", {
    bedrockRegion: "us-east-1",
    selfSignUpEnabled: false,
    enableBotStore: true,
    autoJoinUserGroups: [],
    tokenValidMinutes: 120,
    enableLambdaSnapStart: true,
  });