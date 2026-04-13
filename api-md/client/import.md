---
title: SDK introduction
hide_title: true
sidebar_position: 1
---
  

<Tabs groupId='sdks-language' values={[
  { label: 'Android', value: 'android' },
  { label: 'iOS', value: 'ios' },
  { label: 'JavaScript', value: 'js' },
  { label: 'Flutter', value: 'flutter' },
]}>
  

<TabItem value="android">

1. Import Juggle’s Maven repository. Open `settings.gradle` in the root directory (Project view).

```java
dependencyResolutionManagement {
  repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
  repositories {
    google()
    mavenCentral()
    maven {
      url "https://repo.juggle.im/repository/maven-releases/"
    }
  }
}
```

2. Add the Juggle dependency in your application’s `build.gradle`.

```java
dependencies {
  ...
  api 'com.juggle.im:juggle:1.8.13.2'
}
```

</TabItem>

<TabItem value="ios">

1. Add the following line to your Podfile:

```shell
pod 'JuggleIM', '1.8.13.2'
```

2. Run the following command in the terminal:

```shell
pod install
```

</TabItem>

<TabItem value="js">

```js
npm install jugglechat-websdk --save

import JIM from 'jugglechat-websdk';
```

For detailed examples, please refer to [Quick Start](../../client/quickstart/web/quickstart).

</TabItem>

<TabItem value="flutter">

1. Add the following under `dependencies` in your `pubspec.yaml`:

```yaml
# pubspec.yaml

dependencies:
  juggle_im: 0.0.63
```

2. For detailed examples, please refer to [Quick Start](../../client/quickstart/flutter).

</TabItem>

</Tabs>