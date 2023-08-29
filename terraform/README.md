# Creating an Edu Site on App Engine with Terraform

This is a rough list of steps that need to be completed to configure App Engine with terraform so that it is suitable for deploying the Chainguard Academy site.

First, visit the [billing page](https://console.cloud.google.com/billing) in Google Cloud Console. Copy the `Billing account ID` since you will need to supply it to `terraform`.

1. Create a new project under the Non-Production -> Shared -> App Engine Sites folder. For this guide assume the name `chainguard-academy-dev`.
2. Create a storage bucket to store terraform state files: https://console.cloud.google.com/storage/browser. Call it something meaningful like `jamon-academy-tf-state` to differentiate it from the App Engine files.
3. Enable billing on the bucket at the top of the page. Without this terraform will not run.
4. Edit `providers.tf`. Substitute your bucket name into the `bucket = ...` line.
5. Edit `terraform.tfvars`. Change the `project_id` to the one you created in Step 1, e.g. `chainguard-academy-dev`.
6. Run `terraform init`
7. Import the project that you created in step 1: `terraform import google_project.chainguard-academy-dev chainguard-academy-dev`
8. Run `terraform plan -out plan.out --` to generate a plan. This will not apply the configuration. You will be prompted to enter the Billing Account ID and an Oauth contact email. Alternatively, you can supply these values on the command line by adding `--var billing_account="account_id_goes_here" --var oauth_support_email="email@chainguard.dev"` to the end of the `terraform plan` command.
9. Review the plan carefully. Ensure you are working on the correct project!
10. Run `terraform apply "plan.out"`.
11. Toggle on IAP off, then back on for `App Engine app`: https://console.cloud.google.com/security/iap
12. You may receive errors about Identity-Aware Proxy being disabled like the following. If this happens wait a few minutes, then run `terraform plan -out plan.out` and then `terraform apply "plan.out"` again.

```
Error: Error applying IAM policy for iap web "projects/chainguard-academy-staging/iap_web": Error setting IAM policy for iap web "projects/chainguard-academy-staging/iap_web": googleapi: Error 403: Cloud Identity-Aware Proxy API has not been used in project 293474827457 before or it is disabled.
```

Enable it by visiting https://console.developers.google.com/apis/api/iap.googleapis.com/overview?project=293474827457 then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry

