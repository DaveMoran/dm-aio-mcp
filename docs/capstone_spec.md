# Capstone Domain Decision

## Quesiton to Answer:
Write a 1-page domain brief (audience, problem, why MCP fits) for this project in order to better understand the purpose of this project.

## Answer

### MCP Idea: Personal Dashboard Agent

**Audience**: The audience for this will be two tiered. The first tier of this is a power user (me), who will be interacting with the dashboard every day, utilizing all of the features available and using the built-in chat to interact with all items. The second tier are casual users, those who may only use one aspect of the application (like the shopping list) and are open to the other options. These users may not user all features, but we'll want to make sure the features are still available for them.

This system is meant to help users create goals for themselves by tracking morning/evening routines, nutrition macros, workouts, and todo-lists. As the skeleton is built and data is entered, the MCP servers will allow a chat agent to interact with the application via a non-UI perspective. Instead, they can chat to the agent and it will be able to return all of the information as needed

**Problems**: We'll want to make sure that security is top of mind for this project, especially considering that we're building this tracker with an MCP-first mentality. Supabase (who we're using) was recently in the news due to many vibe-coded applications not having the right security protocols. Even though we're not vibe-coding the MCP portion, the shell of the application is vibe-coded. To help with this we'll create three different users to test authorization/authentication and row level security.

Another problem that we'll have to manage is the ability for the LLM via MCP server to understand CRUD operations that may span different lines. For example, if a user says "Hey, can you let me know if i need to buy anything? I just finished my run for the day". We need to be able to parse these as separate MCP calls and see how that is handled.

We'll be able to handle this during this quarter as we learn more about Evals. Evals will allow us to create tests and scores against potential prompts that a user may give our agent. These evals allow us to create a quantitative measure of following instructions instead of just waving our hands and saying things are non-deterministic and out of our control. This can also introduce us to CI/CD integrations to ensure that any new functionalities dont change thew way our LLM will respond.

**Why MCP**: As this application is built out, it will house a number of API calls that will open up the application for use with things like external APIs or even smart assistants like Siri. By implementing an MCP server, we allow for a user to work with the application via natural language. Additionally, once all MCP servers are built out we can look at shifting the UI to being chat-first as we'll be able to support different types of focus depending on the type of user.

We'll utilize an MCP server over an agent skill or REST as it will provide us a few benefits:
1. Sampling & Elicitation: MCPs allow our server the ability to tell the client that data is missing in order to complete an action. This will allow us to handle edge cases like "What's the weather today" by having it so if an MCP tool/resource is not available we return a response to the user to stay along the lines of the app. We can also do things like "I want to add something to my shoping list" and ask the user what item they want
2. Monitoring: We'll be able to check the request/responses of the MCP Server and when certain tools were chosen to be used. This will give us insight into whether or not we need to add aditional evals or harnesses to the LLM so that it can handle things like multi-request inputs
3. Security: Going through the MCP server gives us a level of obfuscation between the application and the database. That being said, we'll still want to make sure that the MCP server itself has a high level of security so that we do not accidentally edit a row of a different user.

