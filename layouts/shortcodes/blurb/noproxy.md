Zscaler, a popular decrypting proxy, may not support encrypted HTTP/2 traffic by default. If you are having connection
issues using `chainctl` behind Zscaler, follow these steps to enable support for HTTP/2.

1. **Open a Support Ticket with Zscaler**

    Before any UI configuration option appears you may need to contact Zscaler Support (TAC) and request that
    HTTP/2 support be provisioned/activated for your tenant. This is currently a backend setting only support can toggle.

    You typically need to provide:
   * Your Company ID
   * Tenant details
   * Reason/use case for enabling HTTP/2 inspection

   This will allow HTTP/2 negotiation to be available in policies.

2. **Enable HTTP/2 in SSL Inspection Policies**

   Once support has enabled HTTP/2 on your tenant:

   1. Log in to the Zscaler Admin Portal.
   2. Navigate to Policy → SSL Inspection (or Administration → Advanced Settings depending on UI version).
   3. Edit your relevant SSL Inspection Policy.
   4. Look for the option “Enable HTTP/2” and turn it ON for the required rules/policies.

   This setting ensures Zscaler will maintain HTTP/2 where possible rather than downgrading to HTTP/1.1.
   You may need to enable it on multiple rules if you use granular SSL policies (e.g., by URL category).

3. **Check Advanced settings for API/CLI traffic**

    Zscaler has an advanced setting under Admin → Advanced that controls how non-browser (e.g., API/CLI) HTTP/2 traffic is handled.
    This setting is disabled by default, which means Zscaler will downgrade non-browser HTTP/2 traffic to HTTP/1.1. For
    `chainctl` usage, this must be Enabled.

See this [Zscaler blog post for more details](https://www.zscaler.com/blogs/product-insights/http-2-better-faster-stronger).

If the above approach is not available to you, you may need to reconfigure Zscaler to disable its "Block Undecryptable
Traffic" setting. Another option is to configure direct (proxyless) access to HTTP/2 endpoints and use the
`no_proxy` environment variable, depending on your IT policies. Please consult your proxy software's
documentation for guidance on adjusting these settings in order to authenticate.
