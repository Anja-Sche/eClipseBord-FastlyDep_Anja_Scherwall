variable "resource-group-name" {
  default = "rg-fullstack-python"
  type    = string
}

variable "location" {
  type    = string
  default = "belgiumcentral"
}

variable "project_name" {
    default = "eclipseboard"
}

variable "acr_name" {
    default = "acrclipse"
}

variable "image_tag" {
    default = "latest"
}