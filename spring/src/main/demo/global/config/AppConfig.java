package com.example.demo.global.config;

import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;

import java.time.Duration;

/**
 * 앱 전역에서 같이 쓸 객체를 등록한다.
 * @Bean 으로 만든 RestTemplate은 AIClient 생성자에 자동으로 들어간다.
 */
@Configuration
public class AppConfig {

    /** FastAPI 호출용. AI가 느려도 Spring이 무한정 기다리지 않도록 시간 제한을 둔다. */
    @Bean
    public RestTemplate restTemplate(RestTemplateBuilder builder) {
        return builder
                .setConnectTimeout(Duration.ofSeconds(3))
                .setReadTimeout(Duration.ofSeconds(40))
                .build();
    }
}
