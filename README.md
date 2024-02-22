# Task tracker clean architecture
Clean architecture based implementation of a simple task tracker 

## Tracker
Task tracker is just a service used for managing tasks.
A task is an entity that follows some rules:
- it has a description
- it has an id
- it has a determined status (in_backlog, prioritized, in_work, in_review, done)
- it has a creation time
- it has a status update time (it is equal to creation time in the moment of creation)
- first iteration means that task has only one assignee (you)

## Business cases
The tracker must offer some useful functions:
- retrieving task description in upper case by task id (weird, but this is what the boss wants)
- task creation
- changing task status (update time should be refreshed)
- task deletion, if task status is done

Let the magic happen!

## Details
The company can't afford any working server, so you are to use in-memory storage for all the tasks

Also, frontend developer is going to join my team soon, but MVP presentation is so close! 
I have to show all the main features with CLI commands!
