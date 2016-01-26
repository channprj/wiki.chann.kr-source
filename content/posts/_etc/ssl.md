Title: Nginx와 Cloudflare를 이용하여 SSL-Only 설정하기
Slug: ssl-only-nginx-cloudflare
Date: 2015-12-31 20:00
Category: Dev
Tags: dev, server, nginx, ssl, secure
Author: CHANN
<!--Summary: -->

아주 간단하다. `sites-enabled`에 링크해 둔 Nginx 환경설정파일에 아래의 3줄을 추가하면 된다.

```nginx
if ($http_cf_visitor ~ '{"scheme":"http"}') {
  return 301 https://$server_name$request_uri;
}
```

Let's Encrypt를 사용하는 정도의 방법이 있긴 한데, Cloudflare를 사용한다면 위의 방법이 보다 편리하고 나은 선택이 될 수 있다. 인증기간도 더 길고, Nginx 환경설정 파일의 코드 3줄이면 끝나니까.

아래의 참고링크를 누르면 Apache 웹서버에서의 방법도 적혀있다. Nginx에서도 rewrite 룰을 적용해서 SSL-Only를 시도해봤는데, 무한 인다이렉션이 떠서 실패했음. Cloudflare 서비스 방식을 살펴보면 왜 그랬는지는 이해가 간다.

----------

## 참고
1. [Cloudflare 공식 도움말](https://support.cloudflare.com/hc/en-us/articles/200170536-How-do-I-redirect-all-visitors-to-HTTPS-SSL-)
