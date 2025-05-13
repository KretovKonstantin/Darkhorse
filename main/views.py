from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


from market.models import Categories



class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dark horse - Главная'
        context['content'] = "Tattoo market Dark Horse"
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dark horse - О нас'
        context['content'] = "О Dark horse"
        context['text_on_page'] = "Tattoomarket.kz — это казахстанская компания, специализирующаяся на продаже профессионального оборудования и расходных материалов для татуировки и перманентного макияжа. Они являются официальными представителями таких брендов, как AVA, Allegory INK, Ambition, B-Caine, Blackbird, Brand X, Cartel и других."
        return context
    
 # main/views.py


class ContactView(TemplateView):
    template_name = 'main/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dark horse - Контакты'  # Присваиваем title
        context['content'] = "Контактная информация"
        context['text_on_page'] = "Здесь вы можете найти информацию о том, как с нами связаться."
        return context
    



class DeliveryView(TemplateView):
    template_name = 'main/delivery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dark horse - Доставка'
        context['content'] = "Информация о доставке"
        context['text_on_page'] = "Здесь вы найдёте всю информацию по доставке наших товаров."
        return context

