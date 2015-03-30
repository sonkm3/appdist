from django.db import models

import zipfile, plistlib


class DistApp(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()
    package_file = models.FileField(upload_to='public')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True, auto_now=True)

    display = models.BooleanField(default=True,)

    bundle_identifier = models.CharField(max_length=100, null=True, blank=True)
    bundle_version = models.CharField(max_length=100, null=True, blank=True)

    def save(self):
        def get_info_plist(app_file):
            try:
                target_ipa = zipfile.ZipFile(app_file)
                for filename in target_ipa.namelist():
                    if filename.endswith('Info.plist'):
                        info_plist = plistlib.loads(target_ipa.read(filename))
                        if 'CFBundleIdentifier' in info_plist:
                            return info_plist
            except Exception as e:
                raise e # いや。。その。。。

        app_info = get_info_plist(self.package_file.file)

        if app_info:
            self.bundle_identifier = app_info['CFBundleIdentifier']
            self.bundle_version = app_info['CFBundleShortVersionString']
        else:
            pass
        super().save()
