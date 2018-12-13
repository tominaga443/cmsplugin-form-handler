# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms


class FormPluginFormMixin(object):
    def __init__(self, source_url, instance, cmsplugin_form_model_instance=None, **kwargs):
        """
        Extracts what we need from the modified signature, then instantiates
        the form as usual.
        """
        # HACK: Get ModelForm instance from specified keyword and throw to form as instance.
        if cmsplugin_form_model_instance:
            kwargs.update({'instance': cmsplugin_form_model_instance})

        super(FormPluginFormMixin, self).__init__(**kwargs)
        self.fields['cmsplugin_form_source_url'] = forms.CharField(
            widget=forms.HiddenInput, initial=source_url)
        self.plugin_id = instance.pk
