# Test

Cron job that runs on deta.sh which queries metal-joke-api and sends the response as an email

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

### Run Locally

TODO

### Deploy to Deta

TODO

## Testing

```bash
poetry run pytest
```
