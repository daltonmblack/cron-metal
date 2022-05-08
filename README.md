# Cron Metal

Cron job that runs on deta.sh which queries metal-joke-api and sends the response as an email.


## Setup

There are various pieces of this project that can be set up. You should pick which steps are required for your needs/preferences.


### Prerequisites

* [ ] Deta
  * [ ] Account on [deta.sh](https://web.deta.sh/)
  * [ ] Deta CLI tool installed ([Installing the Deta CLI](https://docs.deta.sh/docs/cli/install))
  * [ ] [metal-joke-api](https://github.com/daltonmblack/metal-joke-api) project set up and running in deta.sh
* [ ] SendGrid
  * [ ] SendGrid account with a [verified single sender](https://docs.sendgrid.com/ui/sending-email/sender-verification)
  * [ ] SendGrid email template ([Design a dynamic transactional template](https://docs.sendgrid.com/ui/sending-email/how-to-send-an-email-with-dynamic-transactional-templates#design-a-dynamic-transactional-template))


### First Time Deta Setup

Log into deta.sh

```bash
deta login
```

For anyone other than me (daltonmblack), you'll need to complete the following step. This sets up a new Deta micro application for this project under your control.

```bash
rm -rf cronmetal/.deta
deta new --python --runtime python3.8 cronmetal
```

Deploy the current version of the application to Deta

```
deta deploy cronmetal
```

Verify the application deployed successfully by navigating to [web.deta.sh](https://web.deta.sh/), clicking on `Micros` in the left pane, and checking that an application exists with the name `cronmetal`.


### (Optional) Copy git hooks to local .git/

This project provides templates for git hooks that help to preemptively ensure the quality of commits to the repository, such as sanity checks on the env variable configuration.

To leverage the provided hooks, run the following command from the project's root directory:
```bash
cp hooks/* .git/hooks/
```


### Configure the Application

Create a `.env` file at the root directory based on the `.env_TEMPLATE` file

```
cp .env_TEMPLATE .env
```

Fill in the `PLACEHOLDER` values in the new `.env` file.


## Running the Application

Before running the application (either locally or on Deta), make sure to complete the steps in `Configure the Application` above.

Use either of the two run methods below to trigger SendGrid sending an email to the value of `TO_EMAILS` in your `.env`.


### Run Locally

Trigger SendGrid directly from your local environment using:

```
poetry run python run_locally.py
```


### Deploy to Deta and Enable the Cron Job

Deploy the most up-to-date version of your application:

```
deta deploy cronmetal
```

Set up (or update) the cron job timing that you would like Deta to run your application with:

```
deta cron set cronmetal "<expression>"
```

For a list of valid values for `<expression>` (e.g., `5 hours` to run the job every 5 hours) use:

```
deta cron set --help
```

At this point if the setup was done correctly and your cron job has run for the first time, you should see an email show up in your targeted email address!


## Testing

```bash
poetry run pytest
```
