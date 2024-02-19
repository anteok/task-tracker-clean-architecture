# Task tracker clean architecture
Clean architectrure based implementation of a simple task tracker 

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
- task creation
- changing task status
- task deletion

Let the magic happen!
