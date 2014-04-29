# alsudani

## What is this?

A personal website built using Django

[TODO](todo.md)

## Tenets

- Style reuse should be trivial. I should be able to take the style
  and put it on a different website very easily

- It should only require trivial changes to run on a different service
  (from aws)

## Deployment

It's configured to run automatically on ElasicBeanstalk.

### Steps

- Create a Django ElasticBeanstalk app

- Add environment variable: `ENVIRONMENT='PRODUCTION'`

- Deploy and voila!


## Notes

-
