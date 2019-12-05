pip install django-el-pagination==3.1.0

#settings installed apps
'el-pagination',

#templates before {% for instance in instances %}
{% load el_pagination_tags %}
{% paginate 21 instances %}

#add widget after table container
<!--pagination -->
<div class="bootgrid-footer container-fluid" id="data-table-selection-footer">
    {% get_pages %}
    <div class="row">
        <div class="col-sm-6">
            <div class="pagination">
                {% show_pages %}
            </div>
        </div>
        <div class="col-sm-6 infoBar">
            <div class="infos">
                Showing {{title}} <span class="current_page_index">{{ pages.current_start_index }}</span> - <span class="current_end_status">{{ pages.current_end_index }}</span> of <span class="total_count">{{ pages.total_count }}</span>
            </div>
        </div>
    </div>
</div>
<!--pagination-->

############################################

#templates before for loop ( {% for instance in instances %} ) add -
  {% load el_pagination_tags %}
  {% paginate 21 instances %} # 21 is the number of elements that should be loaded in a page


#add widget after table container
  <!--pagination -->
    {% get_pages %}
      <div class="pagination">
        {% show_pages %}
      </div>
  <!--pagination-->
  
  
#add css for pagination - 
  div.pagination{
    display: flex;
    flex-direction: row;
    justify-content: center;align-items: center;
  }
  div.pagination span.endless_page_current{
    display: inline-block;
    width: 40px;
    height: 40px;
    border-radius: 12px;
    background: linear-gradient(to right, #7eb244, #43C6AC);
    border: 1px solid #afafaf;
    color: #fff;
    padding: 13px 0;
    margin: 0 2.5px;
    box-sizing: border-box;
  }
  div.pagination a.endless_page_link{
    display: inline-block;
    width: 40px;
    height: 40px;
    margin: 0 2.5px;
    border-radius: 12px;
    border: 1px solid #afafaf;
    padding: 13px 0;
    box-sizing: border-box;
  }
