def test_get_new_folder(client):
    # GIVEN: An authenticated API client
    # WHEN: We try to fetch news
    response = client.get('https://6.demo.plone.org/++api++/news')

    # THEN The request is successful and return a folder type
    assert response.status_code == 200
    data = response.json()
    assert data["@type"] == "Folder"


def test_create_news_item(client):
    # GIVEN An authenticated API client
    # WHEN We create news item
    response = client.post('https://6.demo.plone.org/++api++/news',
                           json={'@type': 'Document',
                                 'title': "New Document"}, )
    data = response.json()
    post_id = data['id']

    # THEN We can fetch and delete the news item
    # Fetch the news item
    get_news_item = client.get(f"https://6.demo.plone.org/++api++/news/{post_id}",)
    assert get_news_item.status_code != 404
    get_data = get_news_item.json()
    assert get_data['title'] == 'New Document'

    # Delete the news item
    delete_news_item = client.delete(f"https://6.demo.plone.org/++api++/news/{post_id}",)
    # internet code 204: No Content
    assert delete_news_item.status_code == 204
    get_news_item_after_delete = client.get(f"https://6.demo.plone.org/++api++/news/{post_id}",)
    assert get_news_item_after_delete.status_code == 404
    message_after_delete = get_news_item_after_delete.json()
    assert message_after_delete["type"] == "NotFound"

