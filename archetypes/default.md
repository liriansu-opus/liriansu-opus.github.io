---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: true
# Shared by the zh and en versions of a post; this is what links them.
translationKey: {{ .Name }}
aliases:
  - /{{ .Name }}
---

<!--more-->
