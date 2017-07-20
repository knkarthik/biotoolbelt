from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import RequestFactory
from .acmg_improved import main as acmg


class ACMGTests(TestCase):

    test_post_data = [u'bp1', u'bp4', u'pm3', u'pp1', u'ps4']
    test_template_data = u'Likely Pathogenic'

    def test_homepage(self):
        response = self.client.get(reverse('acmgtool:index'))
        self.assertEqual(response.status_code, 200)

    # def test_post(self):
    #     request_factory = RequestFactory()
    #     request = request_factory.post(reverse('acmgtool:index'), data={'checks': self.test_post_data})
    #     self.assertEqual(request.POST.getlist('checks'), self.test_post_data)

    def test_acmg_classfication(self):
        request = self.client.post(reverse('acmgtool:index'), data={'checks': self.test_post_data})
        # Get only the ACMG codes from the request
        data = request.context['checks'][1]
        self.assertEquals(acmg(data)[0], self.test_template_data)
        self.assertTemplateUsed(request, 'acmgtool/acmg.html')
        self.assertContains(request, self.test_template_data)

