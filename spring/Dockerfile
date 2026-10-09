
# syntax=docker/dockerfile:1

# ============================================================
# Stage 1: Spring Boot 빌드
# ============================================================
FROM eclipse-temurin:17-jdk-jammy AS build

WORKDIR /workspace

COPY gradlew build.gradle settings.gradle ./
COPY gradle ./gradle

RUN chmod +x gradlew

COPY src ./src

RUN ./gradlew --no-daemon clean bootJar -x test


# ============================================================
# Stage 2: 애플리케이션 실행
# ============================================================
FROM eclipse-temurin:17-jre-jammy

WORKDIR /app

RUN groupadd -r spring \
    && useradd -r -g spring spring

COPY --from=build /workspace/build/libs/*.jar /app/app.jar

USER spring

ENV SERVER_PORT=8080
ENV JAVA_OPTS="-XX:MaxRAMPercentage=75"

EXPOSE 8080

ENTRYPOINT ["sh", "-c", "exec java $JAVA_OPTS -jar /app/app.jar"]
