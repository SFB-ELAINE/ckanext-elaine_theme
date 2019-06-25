import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import activity_streams as activity_streams

def resolve_creator_user_id (creator_user_id):
    '''
    Return a dictionary of information about the user with the given creator_id

    :param creator_id: a user ID to resolve
    :type creator_id: string

    :returns: dictionary with details about the user
    :rtype: dictionary
    '''
    user_dict = toolkit.get_action('user_show')(None, data_dict={'id': creator_user_id})
    return user_dict

def user_activity_list_html(context, data_dict):
    '''Return a user's public activity stream as HTML.

    The activity stream is rendered as a snippet of HTML meant to be included
    in an HTML page, i.e. it doesn't have any HTML header or footer.

    Uses custom elaine_activity_list_to_html() function to ensure that revision
    ID is passed to the templates.

    :param id: The id or name of the user.
    :type id: string
    :param offset: where to start getting activity items from
        (optional, default: ``0``)
    :type offset: int
    :param limit: the maximum number of activities to return
        (optional, default: ``31``, the default value is configurable via the
        ckan.activity_list_limit setting)
    :type limit: int

    :rtype: string

    '''
    activity_stream = toolkit.get_action('user_activity_list')(context, data_dict)
    offset = int(data_dict.get('offset', 0))
    extra_vars = {
        'controller': 'user',
        'action': 'activity',
        'id': data_dict['id'],
        'offset': offset,
    }
    # use custom activity_list_to_html function in activity_streams.py
    return activity_streams.elaine_activity_list_to_html(
        context, activity_stream, extra_vars)

def package_activity_list_html(context, data_dict):
    '''Return a package's activity stream as HTML.

    The activity stream is rendered as a snippet of HTML meant to be included
    in an HTML page, i.e. it doesn't have any HTML header or footer.

    Uses custom elaine_activity_list_to_html() function to ensure that revision
    ID is passed to the templates.

    :param id: the id or name of the package
    :type id: string
    :param offset: where to start getting activity items from
        (optional, default: ``0``)
    :type offset: int
    :param limit: the maximum number of activities to return
        (optional, default: ``31``, the default value is configurable via the
        ckan.activity_list_limit setting)
    :type limit: int

    :rtype: string

    '''
    activity_stream = toolkit.get_action('package_activity_list')(context, data_dict)
    offset = int(data_dict.get('offset', 0))
    extra_vars = {
        'controller': 'package',
        'action': 'activity',
        'id': data_dict['id'],
        'offset': offset,
    }
    # use custom activity_list_to_html function in activity_streams.py
    return activity_streams.elaine_activity_list_to_html(
        context, activity_stream, extra_vars)

def group_activity_list_html(context, data_dict):
    '''Return a group's activity stream as HTML.

    The activity stream is rendered as a snippet of HTML meant to be included
    in an HTML page, i.e. it doesn't have any HTML header or footer.

    Uses custom elaine_activity_list_to_html() function to ensure that revision
    ID is passed to the templates.

    :param id: the id or name of the group
    :type id: string
    :param offset: where to start getting activity items from
        (optional, default: ``0``)
    :type offset: int
    :param limit: the maximum number of activities to return
        (optional, default: ``31``, the default value is configurable via the
        ckan.activity_list_limit setting)
    :type limit: int

    :rtype: string

    '''
    activity_stream = toolkit.get_action('group_activity_list')(context, data_dict)
    offset = int(data_dict.get('offset', 0))
    extra_vars = {
        'controller': 'group',
        'action': 'activity',
        'id': data_dict['id'],
        'offset': offset,
    }
    # use custom activity_list_to_html function in activity_streams.py
    return activity_streams.elaine_activity_list_to_html(
        context, activity_stream, extra_vars)

def organization_activity_list_html(context, data_dict):
    '''Return a organization's activity stream as HTML.

    The activity stream is rendered as a snippet of HTML meant to be included
    in an HTML page, i.e. it doesn't have any HTML header or footer.

    Uses custom elaine_activity_list_to_html() function to ensure that revision
    ID is passed to the templates.

    :param id: the id or name of the organization
    :type id: string

    :rtype: string

    '''
    activity_stream = toolkit.get_action('organization_activity_list')(context, data_dict)
    offset = int(data_dict.get('offset', 0))
    extra_vars = {
        'controller': 'organization',
        'action': 'activity',
        'id': data_dict['id'],
        'offset': offset,
    }
    # use custom activity_list_to_html function in activity_streams.py
    return activity_streams.elaine_activity_list_to_html(
        context, activity_stream, extra_vars)

def recently_changed_packages_activity_list_html(context, data_dict):
    '''Return the activity stream of all recently changed packages as HTML.

    The activity stream includes all recently added or changed packages. It is
    rendered as a snippet of HTML meant to be included in an HTML page, i.e. it
    doesn't have any HTML header or footer.

    Uses custom elaine_activity_list_to_html() function to ensure that revision
    ID is passed to the templates.

    :param offset: where to start getting activity items from
        (optional, default: ``0``)
    :type offset: int
    :param limit: the maximum number of activities to return
        (optional, default: ``31``, the default value is configurable via the
        ckan.activity_list_limit setting)
    :type limit: int

    :rtype: string

    '''
    activity_stream = toolkit.get_action('recently_changed_packages_activity_list')(
        context, data_dict)
    offset = int(data_dict.get('offset', 0))
    extra_vars = {
        'controller': 'package',
        'action': 'activity',
        'offset': offset,
    }
    # use custom activity_list_to_html function in activity_streams.py
    return activity_streams.elaine_activity_list_to_html(
        context, activity_stream, extra_vars)

def dashboard_activity_list_html(context, data_dict):
    '''Return the authorized (via login or API key) user's dashboard activity
       stream as HTML.

    The activity stream is rendered as a snippet of HTML meant to be included
    in an HTML page, i.e. it doesn't have any HTML header or footer.

    Uses custom elaine_activity_list_to_html() function to ensure that revision
    ID is passed to the templates.

    :param offset: where to start getting activity items from
        (optional, default: ``0``)
    :type offset: int
    :param limit: the maximum number of activities to return
        (optional, default: ``31``, the default value is configurable via the
        ckan.activity_list_limit setting)
    :type limit: int

    :rtype: string

    '''
    activity_stream = toolkit.get_action('dashboard_activity_list')(context, data_dict)
    model = context['model']
    user_id = context['user']
    offset = data_dict.get('offset', 0)
    extra_vars = {
        'controller': 'user',
        'action': 'dashboard',
        'offset': offset,
        'id': user_id
    }
    # use custom activity_list_to_html function in activity_streams.py
    return activity_streams.elaine_activity_list_to_html(context, activity_stream,
                                                  extra_vars)


class ElaineThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # Declare that this plugin will implement ITemplateHelpers and IActions
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IActions)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'elaine_theme')

    # ITemplateHelpers

    def get_helpers(self):
        '''
        Register the plugin's helper functions.
        '''
        return {'elaine_theme_resolve_creator_user_id': resolve_creator_user_id}

    # IActions

    def get_actions(self):
        return {'user_activity_list_html': user_activity_list_html,
                'package_activity_list_html': package_activity_list_html,
                'group_activity_list_html': group_activity_list_html,
                'organization_activity_list_html': organization_activity_list_html,
                'recently_changed_packages_activity_list_html': recently_changed_packages_activity_list_html,
                'dashboard_activity_list_html': dashboard_activity_list_html}
