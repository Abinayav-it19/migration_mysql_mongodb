# website_document = {
#                     "showcase_id": row['showcase_id'],
#                     "com_id": row['com_id'],
#                     "showcase_name": row['showcase_name'],
#                     "old_domain_name": row['old_domain_name'],
#                     "free_showcase_name": row['free_showcase_name'],
#                     "selected_date": row['selected_date'],
#                     "published_date": row['published_date'],
#                     "modified_date": row['modified_date'],
#                     "hosted_date": row['hosted_date'],
#                     "status": row['status'],
#                     "membership_status": row['membership_status'],
#                     "web_banner": {
#                         "web_home_banner1": row['web_home_banner1'],
#                         "web_home_banner2": row['web_home_banner2'],
#                         "web_home_banner3": row['web_home_banner3'],
#                         "web_profile_banner": row['web_profile_banner'],
#                         "web_product_index_banner": row['web_product_index_banner'],
#                         "web_groups": row['web_groups'],
#                         "web_group_banners": row['web_group_banners'],
#                         "group_banner": row['group_banner'],
#                         "web_contact_banner": row['web_contact_banner']
#                     },
#                     "template": {
#                         "template_id": row['template_id'],
#                         "template_name": row['template_name'],
#                         "layout_id": row['layout_id']
#                     },
#                     "layout": {
#                         "layout_id": row['layout_id'],
#                         "banner_width": row['banner_width'],
#                         "banner_height": row['banner_height'],
#                         "product_width": row['product_width'],
#                         "product_height": row['product_height'],
#                         "create_user_id": row['create_user_id'],
#                         "created_date": row['created_date'],
#                         "modified_date": row['modified_date'],
#                         "status": row['status']
#                     }
#                 }


# SELECT 
#             s.showcase_id, 
#             s.com_id, 
#             s.showcase_name, 
#             s.old_domain_name, 
#             s.free_showcase_name, 
#             s.selected_date, 
#             s.published_date, 
#             s.modified_date, 
#             s.hosted_date, 
#             s.status, 
#             s.membership_status,
#             b.web_home_banner1, 
#             b.web_home_banner2, 
#             b.web_home_banner3, 
#             b.web_profile_banner, 
#             b.web_product_index_banner, 
#             b.web_groups, 
#             b.web_group_banners, 
#             b.group_banner, 
#             b.web_contact_banner,
#             t.template_id, 
#             t.template_name, 
#             t.layout_id,
#             l.banner_width, 
#             l.banner_height, 
#             l.product_width, 
#             l.product_height, 
#             l.create_user_id, 
#             l.created_date, 
#             l.modified_date, 
#             l.status
#             FROM 
#                 web_showcase s
#             LEFT JOIN 
#                 web_banners b ON s.com_id = b.com_id
#             LEFT JOIN 
#                 web_template t ON s.template_id = t.template_id
#             LEFT JOIN 
#                 web_layouts l ON t.layout_id = l.layout_id