# Dawn section 原生结构

用于确认采用 Dawn 原生约定的内容模块。纯图片模块省略标题、描述及相应设置；通栏遵循明确的媒体需求。

```liquid
{%- style -%}
  .section-{{ section.id }}-padding {
    padding-top: {{ section.settings.padding_top | times: 0.75 | round: 0 }}px;
    padding-bottom: {{ section.settings.padding_bottom | times: 0.75 | round: 0 }}px;
  }
  @media screen and (min-width: 750px) {
    .section-{{ section.id }}-padding {
      padding-top: {{ section.settings.padding_top }}px;
      padding-bottom: {{ section.settings.padding_bottom }}px;
    }
  }
{%- endstyle -%}
<div class="section-{{ section.id }}-padding color-{{ section.settings.color_scheme }} gradient">
  <div class="page-width">
    {%- unless section.settings.heading == blank -%}
      <div class="title-wrapper title-wrapper--no-top-margin{% if settings.animations_reveal_on_scroll %} scroll-trigger animate--slide-in{% endif %}">
        <h2 class="title inline-richtext {{ section.settings.heading_size }}">{{ section.settings.heading }}</h2>
        {% if section.settings.content != blank %}<p>{{ section.settings.content | escape }}</p>{% endif %}
      </div>
    {%- endunless -%}
    <!-- Module content -->
  </div>
</div>
{% schema %}
{
  "name": "Native content",
  "settings": [
    {
      "type": "inline_richtext",
      "id": "heading",
      "label": "Heading"
    },
    {
      "type": "color_scheme",
      "id": "color_scheme",
      "label": "t:sections.all.colors.label",
      "default": "scheme-1"
    },
    {
      "type": "range",
      "id": "padding_top",
      "min": 0,
      "max": 100,
      "step": 4,
      "unit": "px",
      "label": "t:sections.all.padding.padding_top",
      "default": 36
    },
    {
      "type": "textarea",
      "id": "content",
      "label": "Content"
    },
    {
      "type": "range",
      "id": "padding_bottom",
      "min": 0,
      "max": 100,
      "step": 4,
      "unit": "px",
      "label": "t:sections.all.padding.padding_bottom",
      "default": 36
    },
    {
      "type": "select",
      "id": "heading_size",
      "label": "t:sections.all.heading_size.label",
      "default": "h1",
      "options": [
        {
          "value": "h2",
          "label": "t:sections.all.heading_size.options__1.label"
        },
        {
          "value": "h1",
          "label": "t:sections.all.heading_size.options__2.label"
        },
        {
          "value": "h0",
          "label": "t:sections.all.heading_size.options__3.label"
        },
        {
          "value": "hxl",
          "label": "t:sections.all.heading_size.options__4.label"
        },
        {
          "value": "hxxl",
          "label": "t:sections.all.heading_size.options__5.label"
        }
      ]
    }
  ]
}
{% endschema %}
```
